# -*- coding: utf-8 -*-

from capsul.api import Pipeline
import traits.api as traits


class Face_spm_categorical_stats(Pipeline):

    def pipeline_definition(self):
        # nodes
        self.add_process("level1design_1", "mia_processes.bricks.stat.spm.model.Level1Design")
        self.add_process("estimatemodel_1", "mia_processes.bricks.stat.spm.model.EstimateModel")

        # links
        self.export_parameter("level1design_1", "timing_units", is_optional=True)
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
        self.export_parameter("level1design_1", "sess_multi", is_optional=True)
        self.export_parameter("level1design_1", "sess_regress", is_optional=True)
        self.export_parameter("level1design_1", "sess_multi_reg", is_optional=True)
        self.export_parameter("level1design_1", "sess_hpf", is_optional=True)
        self.export_parameter("estimatemodel_1", "factor_info", is_optional=True)
        self.add_link("factor_info->level1design_1.factor_info")
        self.export_parameter("estimatemodel_1", "bases", is_optional=True)
        self.add_link("bases->level1design_1.bases")
        self.export_parameter("level1design_1", "volterra_expansion_order", is_optional=True)
        self.export_parameter("level1design_1", "global_intensity_normalization", is_optional=True)
        self.export_parameter("level1design_1", "mask_threshold", is_optional=True)
        self.export_parameter("level1design_1", "mask_image", is_optional=True)
        self.export_parameter("level1design_1", "model_serial_correlations", is_optional=True)
        self.export_parameter("level1design_1", "dict4runtime", is_optional=True)
        self.add_link("level1design_1.spm_mat_file->estimatemodel_1.spm_mat_file")
        self.export_parameter("estimatemodel_1", "out_spm_mat_file", is_optional=False)
        self.export_parameter("estimatemodel_1", "beta_images", is_optional=True)
        self.export_parameter("estimatemodel_1", "residual_image", is_optional=True)
        self.export_parameter("estimatemodel_1", "RPVimage", is_optional=True)
        self.export_parameter("estimatemodel_1", "con_images", is_optional=True)
        self.export_parameter("estimatemodel_1", "spmT_images", is_optional=True)
        self.export_parameter("estimatemodel_1", "ess_images", is_optional=True)
        self.export_parameter("estimatemodel_1", "spmF_images", is_optional=True)

        # parameters order

        self.reorder_traits(("timing_units", "interscan_interval", "microtime_resolution", "microtime_onset", "sess_scans", "sess_cond_names", "sess_cond_onsets", "sess_cond_durations", "sess_cond_tmod", "sess_cond_pmod_names", "sess_cond_pmod_values", "sess_cond_pmod_polys", "sess_cond_orth", "sess_multi", "sess_regress", "sess_multi_reg", "sess_hpf", "factor_info", "bases", "volterra_expansion_order", "global_intensity_normalization", "mask_threshold", "mask_image", "model_serial_correlations", "dict4runtime", "out_spm_mat_file", "beta_images", "residual_image", "RPVimage", "con_images", "spmT_images", "ess_images", "spmF_images"))

        # default and initial values
        self.interscan_interval = 2.0
        self.microtime_resolution = 24
        self.microtime_onset = 12
        self.sess_cond_names = [['N1', 'N2', 'F1', 'F2']]
        self.sess_cond_onsets = [[[6.74996667, 15.74996667, 17.99996667, 26.99996667, 29.24996667, 31.49996667, 35.99996667, 42.74996667, 65.24996667, 67.49996667, 74.24996667, 92.24996667, 112.49996667, 119.24996667, 123.74996667, 125.99996667, 137.24996667, 141.74996667, 143.99996667, 146.24996667, 155.24996667, 159.74996667, 161.99996667, 164.24996667, 204.74996667, 238.49996667], [13.49996667, 40.49996667, 47.24996667, 56.24996667, 89.99996667, 94.49996667, 96.74996667, 134.99996667, 148.49996667, 184.49996667, 191.24996667, 202.49996667, 215.99996667, 233.99996667, 236.24996667, 242.99996667, 245.24996667, 256.49996667, 260.99996667, 281.24996667, 290.24996667, 303.74996667, 310.49996667, 319.49996667, 339.74996667, 341.99996667], [-3.33333333e-05, 2.24996667, 8.99996667, 11.2499667, 22.4999667, 44.9999667, 51.7499667, 60.7499667, 62.9999667, 76.4999667, 78.7499667, 85.4999667, 98.9999667, 101.249967, 103.499967, 116.999967, 130.499967, 150.749967, 170.999967, 188.999967, 227.249967, 265.499967, 283.499967, 285.749967, 287.999967, 344.249967], [33.74996667, 49.49996667, 105.74996667, 152.99996667, 157.49996667, 168.74996667, 177.74996667, 179.99996667, 182.24996667, 197.99996667, 222.74996667, 240.74996667, 254.24996667, 267.74996667, 269.99996667, 274.49996667, 294.74996667, 299.24996667, 301.49996667, 314.99996667, 317.24996667, 326.24996667, 332.99996667, 335.24996667, 337.49996667, 346.49996667]]]
        self.sess_cond_durations = [[[0.0], [0.0], [0.0], [0.0]]]
        self.sess_cond_tmod = [[0, 0, 0, 0]]
        self.sess_cond_orth = [[1, 1, 1, 1]]
        self.sess_hpf = [128.0]
        self.factor_info = [{'name': 'Fame', 'levels': 2}, {'name': 'Rep', 'levels': 2}]
        self.bases = {'hrf': {'derivs': [1, 1]}}

        # nodes positions
        self.node_position = {
            "level1design_1": (-212.0, -232.0),
            "inputs": (-564.6089343996646, -217.0),
            "estimatemodel_1": (204.0, 16.0),
            "outputs": (629.9090429185574, 82.0),
        }

        # nodes dimensions
        self.node_dimension = {
            "level1design_1": (352.03125, 880.0),
            "inputs": (257.984375, 880.0),
            "estimatemodel_1": (306.53125, 390.0),
            "outputs": (155.64929503946317, 320.0),
        }

        self.do_autoexport_nodes_parameters = False
