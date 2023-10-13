# -*- coding: utf-8 -*-

from capsul.api import Pipeline
import traits.api as traits


class Face_spm_parametric_stats_ok(Pipeline):

    def pipeline_definition(self):
        # nodes
        self.add_process("level1design_1", "mia_processes.bricks.stat.spm.model.Level1Design")
        self.add_process("estimatemodel_1", "mia_processes.bricks.stat.spm.model.EstimateModel")
        self.add_process("estimatecontrast_1", "mia_processes.bricks.stat.spm.model.EstimateContrast")
        self.add_process("concat_to_list_1", "mia_processes.bricks.tools.tools.Concat_to_list")
        self.add_process("concat_to_list_2", "mia_processes.bricks.tools.tools.Concat_to_list")
        self.add_process("concat_to_list_3", "mia_processes.bricks.tools.tools.Concat_to_list")
        self.add_process("concat_to_list_4", "mia_processes.bricks.tools.tools.Concat_to_list")
        self.add_process("files_to_list_1", "mia_processes.bricks.tools.tools.Files_To_List")
        self.add_process("files_to_list_2", "mia_processes.bricks.tools.tools.Files_To_List")

        # links
        self.export_parameter("level1design_1", "interscan_interval", is_optional=True)
        self.export_parameter("level1design_1", "microtime_resolution", is_optional=True)
        self.export_parameter("level1design_1", "microtime_onset", is_optional=True)
        self.export_parameter("level1design_1", "sess_scans", is_optional=False)
        self.export_parameter("level1design_1", "sess_cond_names", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_onsets", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_durations", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_tmod", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_pmod_names", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_pmod_values", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_pmod_polys", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_orth", is_optional=True)
        self.export_parameter("level1design_1", "sess_multi_reg", is_optional=True)
        self.export_parameter("level1design_1", "sess_hpf", is_optional=True)
        self.export_parameter("level1design_1", "factor_info", is_optional=True)
        self.add_link("factor_info->estimatemodel_1.factor_info")
        self.export_parameter("estimatemodel_1", "bases", is_optional=True)
        self.add_link("bases->level1design_1.bases")
        self.export_parameter("estimatecontrast_1", "T_contrast_names", is_optional=True)
        self.export_parameter("estimatecontrast_1", "T_condition_names", is_optional=True)
        self.export_parameter("estimatecontrast_1", "T_contrast_weights", is_optional=True)
        self.export_parameter("estimatecontrast_1", "F_contrast_names", is_optional=True)
        self.export_parameter("estimatecontrast_1", "F_contrast_T_names", is_optional=True)
        self.add_link("level1design_1.spm_mat_file->estimatemodel_1.spm_mat_file")
        self.add_link("estimatemodel_1.out_spm_mat_file->estimatecontrast_1.spm_mat_file")
        self.add_link("estimatemodel_1.beta_images->estimatecontrast_1.beta_images")
        self.add_link("estimatemodel_1.residual_image->estimatecontrast_1.residual_image")
        self.add_link("estimatemodel_1.con_images->concat_to_list_1.list1")
        self.add_link("estimatemodel_1.spmT_images->concat_to_list_2.list1")
        self.add_link("estimatemodel_1.ess_images->concat_to_list_3.list1")
        self.add_link("estimatemodel_1.spmF_images->concat_to_list_4.list1")
        self.add_link("estimatecontrast_1.con_images->concat_to_list_1.list2")
        self.add_link("estimatecontrast_1.spmT_images->concat_to_list_2.list2")
        self.add_link("estimatecontrast_1.ess_images->files_to_list_2.file1")
        self.add_link("estimatecontrast_1.spmF_images->files_to_list_1.file1")
        self.export_parameter("estimatecontrast_1", "out_spm_mat_file", is_optional=False)
        self.export_parameter("concat_to_list_1", "out_list", "con_images", is_optional=False)
        self.export_parameter("concat_to_list_2", "out_list", "spmT_images", is_optional=False)
        self.export_parameter("concat_to_list_3", "out_list", "ess_images", is_optional=False)
        self.export_parameter("concat_to_list_4", "out_list", "spmF_images", is_optional=False)
        self.add_link("files_to_list_1.file_list->concat_to_list_4.list2")
        self.add_link("files_to_list_2.file_list->concat_to_list_3.list2")

        # parameters order

        self.reorder_traits(("interscan_interval", "microtime_resolution", "microtime_onset", "sess_scans", "sess_cond_names", "sess_cond_onsets", "sess_cond_durations", "sess_cond_tmod", "sess_cond_pmod_names", "sess_cond_pmod_values", "sess_cond_pmod_polys", "sess_cond_orth", "sess_multi_reg", "sess_hpf", "factor_info", "bases", "T_contrast_names", "T_condition_names", "T_contrast_weights", "F_contrast_names", "F_contrast_T_names", "con_images", "spmT_images", "ess_images", "spmF_images", "out_spm_mat_file"))

        # default and initial values
        self.interscan_interval = 2.0
        self.microtime_resolution = 24
        self.microtime_onset = 12
        self.sess_cond_names = [['N1', 'N2', 'F1', 'F2']]
        self.sess_cond_onsets = [[[6.74996667, 15.74996667, 17.99996667, 26.99996667, 29.24996667, 31.49996667, 35.99996667, 42.74996667, 65.24996667, 67.49996667, 74.24996667, 92.24996667, 112.49996667, 119.24996667, 123.74996667, 125.99996667, 137.24996667, 141.74996667, 143.99996667, 146.24996667, 155.24996667, 159.74996667, 161.99996667, 164.24996667, 204.74996667, 238.49996667], [13.49996667, 40.49996667, 47.24996667, 56.24996667, 89.99996667, 94.49996667, 96.74996667, 134.99996667, 148.49996667, 184.49996667, 191.24996667, 202.49996667, 215.99996667, 233.99996667, 236.24996667, 242.99996667, 245.24996667, 256.49996667, 260.99996667, 281.24996667, 290.24996667, 303.74996667, 310.49996667, 319.49996667, 339.74996667, 341.99996667], [-3.33333333e-05, 2.24996667, 8.99996667, 11.2499667, 22.4999667, 44.9999667, 51.7499667, 60.7499667, 62.9999667, 76.4999667, 78.7499667, 85.4999667, 98.9999667, 101.249967, 103.499967, 116.999967, 130.499967, 150.749967, 170.999967, 188.999967, 227.249967, 265.499967, 283.499967, 285.749967, 287.999967, 344.249967], [33.74996667, 49.49996667, 105.74996667, 152.99996667, 157.49996667, 168.74996667, 177.74996667, 179.99996667, 182.24996667, 197.99996667, 222.74996667, 240.74996667, 254.24996667, 267.74996667, 269.99996667, 274.49996667, 294.74996667, 299.24996667, 301.49996667, 314.99996667, 317.24996667, 326.24996667, 332.99996667, 335.24996667, 337.49996667, 346.49996667]]]
        self.sess_cond_durations = [[[0.0], [0.0], [0.0], [0.0]]]
        self.sess_cond_tmod = [[0, 0, 0, 0]]
        self.sess_cond_pmod_names = [[None, ['Lag'], None, ['Lag']]]
        self.sess_cond_pmod_values = [[None, [[3.0, 3.0, 10.0, 10.0, 14.0, 1.0, 23.0, 3.0, 3.0, 37.0, 10.0, 42.0, 61.0, 33.0, 27.0, 61.0, 28.0, 22.0, 39.0, 37.0, 62.0, 37.0, 20.0, 54.0, 34.0, 50.0]], None, [[11.0, 14.0, 2.0, 47.0, 36.0, 18.0, 37.0, 59.0, 11.0, 56.0, 33.0, 4.0, 57.0, 18.0, 59.0, 55.0, 46.0, 61.0, 4.0, 67.0, 9.0, 63.0, 13.0, 19.0, 42.0, 1.0]]]]
        self.sess_cond_pmod_polys = [[None, [2], None, [2]]]
        self.sess_cond_orth = [[1, 1, 1, 1]]
        self.sess_hpf = [128.0]
        self.factor_info = [{'name': 'Fame', 'levels': 2}, {'name': 'Rep', 'levels': 2}]
        self.bases = {'hrf': {'derivs': [0, 0]}}
        self.T_contrast_names = ['Famous_lag1', 'Famous_lag2']
        self.T_condition_names = [['F2xLag^1'], ['F2xLag^2']]
        self.T_contrast_weights = [[1.0], [1.0]]
        self.F_contrast_names = ['Famous Lag']
        self.F_contrast_T_names = [['Famous_lag1', 'Famous_lag2']]

        # nodes positions
        self.node_position = {
            "level1design_1": (-1010.0, -231.0),
            "estimatemodel_1": (-574.0, -189.0),
            "estimatecontrast_1": (-458.0, 272.0),
            "inputs": (-1272.1875, -133.0),
            "concat_to_list_1": (135.0, -177.0),
            "outputs": (358.04966791855725, 141.0),
            "concat_to_list_2": (138.0, -48.0),
            "concat_to_list_3": (146.0, 70.0),
            "concat_to_list_4": (147.0, 196.0),
            "files_to_list_1": (-27.0, 496.0),
            "files_to_list_2": (-37.0, 311.0),
        }

        # nodes dimensions
        self.node_dimension = {
            "level1design_1": (400.03125, 880.0),
            "estimatemodel_1": (303.53125, 390.0),
            "estimatecontrast_1": (325.0625, 425.0),
            "inputs": (196.296875, 775.0),
            "concat_to_list_1": (118.4375, 110.0),
            "outputs": (151.265625, 215.0),
            "concat_to_list_2": (118.4375, 110.0),
            "concat_to_list_3": (118.4375, 110.0),
            "concat_to_list_4": (118.4375, 110.0),
            "files_to_list_1": (118.8125, 145.0),
            "files_to_list_2": (121.8125, 145.0),
        }

        self.do_autoexport_nodes_parameters = False
