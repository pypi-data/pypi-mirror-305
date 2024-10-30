import os
from typing import Union, Optional, Iterable
import numpy as np

from simba.mixins.config_reader import ConfigReader
from simba.utils.read_write import find_files_of_filetypes_in_directory, find_video_of_file, get_fn_ext, read_df, read_video_info, read_frm_of_video
from simba.utils.checks import check_all_file_names_are_represented_in_video_log, check_valid_dataframe
from simba.utils.enums import Formats
from simba.video_processors.video_processing import video_bg_substraction_mp
from simba.mixins.geometry_mixin import GeometryMixin
from simba.mixins.image_mixin import ImageMixin
from simba.plotting.geometry_plotter import GeometryPlotter

class MitraTailAnalyzer(ConfigReader):

    def __init__(self,
                 config_path: Union[str, os.PathLike],
                 anchor_points: Iterable[str],
                 body_parts: Iterable[str],
                 data_dir: Optional[Union[str, os.PathLike]] = None,
                 video_dir: Optional[Union[str, os.PathLike]] = None):

        ConfigReader.__init__(self, config_path=config_path, read_video_info=True, create_logger=False)
        if data_dir is None:
            self.data_paths = find_files_of_filetypes_in_directory(directory=self.outlier_corrected_dir, extensions=['.csv'])
        else:
            self.data_paths = find_files_of_filetypes_in_directory(directory=data_dir, extensions=['.csv'])
        if video_dir is not None:
            self.video_dir = video_dir
        self.paths = {}
        for data_path in self.data_paths:
            video = find_video_of_file(video_dir=self.video_dir, filename=get_fn_ext(filepath=data_path)[1])
            self.paths[data_path] = video
        check_all_file_names_are_represented_in_video_log(video_info_df=self.video_info_df, data_paths=self.data_paths)
        self.tail_cols, self.bp_cols = [], []
        for bp in anchor_points:
            self.tail_cols.append(f'{bp}_x'.lower()); self.tail_cols.append(f'{bp}_y'.lower())
        for bp in body_parts:
            self.bp_cols.append(f'{bp}_x'.lower()); self.bp_cols.append(f'{bp}_y'.lower())
        self.required_cols = self.tail_cols + self.bp_cols
        self.bg_temp_dir = os.path.join(data_dir, f'bg_temp')


    def run(self):
        for file_cnt, (file_path, video_path) in enumerate(self.paths.items()):
            _, video_name, _ = get_fn_ext(filepath=file_path)
            _, px_per_mm, fps = read_video_info(vid_info_df=self.video_info_df, video_name=video_name)
            print(f'Analyzing {video_name} ({file_cnt+1}/{len(self.data_paths)})...')
            df = read_df(file_path=file_path, file_type=self.file_type)
            df.columns = [str(x).lower() for x in df.columns]
            check_valid_dataframe(df=df, valid_dtypes=Formats.NUMERIC_DTYPES.value, required_fields=self.required_cols)

            tail_geometry_df = df[self.tail_cols].values.reshape(len(df), int(len(self.tail_cols) /2), 2).astype(np.int64)
            tail_geometries = GeometryMixin().bodyparts_to_polygon(data=tail_geometry_df, parallel_offset=35, pixels_per_mm=px_per_mm)


            hull_geometry_df = df[self.bp_cols].values.reshape(len(df), int(len(self.bp_cols) / 2), 2).astype(np.int64)
            hull_geometries = GeometryMixin().bodyparts_to_polygon(data=hull_geometry_df, parallel_offset=40, pixels_per_mm=px_per_mm)

            union_shapes = GeometryMixin().multiframe_union(shapes=np.array([hull_geometries, tail_geometries]).T)
            # #
            # # for idx in range(len(union_shapes)):
            # #     img = read_frm_of_video(video_path=r"D:\troubleshooting\mitra\project_folder\videos\rotated\592_MA147_CNO1_0515.mp4", frame_index=idx,)
            #
            #
            # print(video_path)
            # plotter = GeometryPlotter(config_path=self.config_path,
            #                           geometries=[union_shapes],
            #                           palette='Pastel1',
            #                           thickness=5, video_name=video_path, save_path=r'D:\troubleshooting\mitra\project_folder\videos\bg_removed\rotated\tail\test.mp4')
            # plotter.run()


            imgs = ImageMixin().slice_shapes_in_imgs(imgs=video_path, shapes=tail_geometries)
            _ = ImageMixin.img_stack_to_video(imgs=imgs,
                                              fps=fps,
                                              save_path=r"D:\troubleshooting\mitra\project_folder\videos\bg_removed\rotated\tail\test.mp4")



            # #geometry_statistics = GeometryMixin.get_shape_statistics(shapes=geometries)
            #
            # # anchor_location = np.array((150, 150)) #X and Y
            # # #anchor_location = np.array((int(geometry_statistics['max_width']), int(geometry_statistics['max_length'] / 2)))
            # # anchor = df[self.anchor_point].values.astype(np.int32)
            # # non_anchor = df[self.non_anchor_points].values.astype(np.int32).reshape(-1, 2, 2)
            # # non_anchor = self._transform_points(anchor_data=anchor, body_parts_data=non_anchor, anchor_location=anchor_location)
            # # arr_3d_extended = np.array([np.vstack((non_anchor[i], anchor_location)) for i in range(non_anchor.shape[0])])
            # # geometries = GeometryMixin().multiframe_bodyparts_to_polygon(data=arr_3d_extended, parallel_offset=3, pixels_per_mm=px_per_mm)
            # #
            # #
            # # s = (int(geometry_statistics['max_length'] / 2) , int(geometry_statistics['max_width']))
            # GeometryMixin.geometry_video(shapes=[geometries],
            #                              size=(300, 300), # Y and X
            #                              save_path=r"C:\troubleshooting\mitra\project_folder\csv\outlier_corrected_movement_location\test\bg_temp\tail.mp4",
            #                              fps=fps, verbose=True, thickness=4)
            #


















runner = MitraTailAnalyzer(config_path=r"D:\troubleshooting\mitra\project_folder\project_config.ini",
                           data_dir=r'D:\troubleshooting\mitra\project_folder\videos\bg_removed\rotated\temp',
                           video_dir=r'D:\troubleshooting\mitra\project_folder\videos\bg_removed\rotated\temp',
                           anchor_points=('tail_base', 'tail_center', 'tail_tip'),
                           body_parts=('nose', 'left_ear', 'right_ear', 'right_side', 'left_side', 'tail_base'))
runner.run()