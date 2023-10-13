# -*- coding: utf-8 -*-

from capsul.api import Pipeline
import traits.api as traits


class Flanker_test_sub08_stats(Pipeline):

    def pipeline_definition(self):
        # nodes
        self.add_process("level1design_1", "mia_processes.bricks.stat.spm.model.Level1Design")
        self.add_process("estimatemodel_1", "mia_processes.bricks.stat.spm.model.EstimateModel")
        self.add_process("estimatecontrast_1", "mia_processes.bricks.stat.spm.model.EstimateContrast")

        # links
        self.export_parameter("level1design_1", "timing_units", is_optional=True)
        self.export_parameter("level1design_1", "interscan_interval", is_optional=True)
        self.export_parameter("level1design_1", "sess_scans", is_optional=False)
        self.export_parameter("level1design_1", "sess_cond_names", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_onsets", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_tmod", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_orth", is_optional=True)
        self.export_parameter("level1design_1", "sess_hpf", is_optional=True)
        self.export_parameter("estimatecontrast_1", "T_contrast_names", is_optional=True)
        self.export_parameter("estimatecontrast_1", "T_condition_names", is_optional=True)
        self.export_parameter("estimatecontrast_1", "T_contrast_weights", is_optional=True)
        self.export_parameter("level1design_1", "sess_cond_durations", is_optional=True)
        self.add_link("level1design_1.spm_mat_file->estimatemodel_1.spm_mat_file")
        self.add_link("estimatemodel_1.out_spm_mat_file->estimatecontrast_1.spm_mat_file")
        self.add_link("estimatemodel_1.beta_images->estimatecontrast_1.beta_images")
        self.add_link("estimatemodel_1.residual_image->estimatecontrast_1.residual_image")
        self.export_parameter("estimatecontrast_1", "con_images", is_optional=True)
        self.export_parameter("estimatecontrast_1", "spmT_images", is_optional=True)
        self.export_parameter("estimatecontrast_1", "out_spm_mat_file", is_optional=False)

        # parameters order

        self.reorder_traits(("out_spm_mat_file", "con_images", "spmT_images", "timing_units", "interscan_interval", "sess_scans", "sess_cond_names", "sess_cond_onsets", "sess_cond_tmod", "sess_cond_orth", "sess_hpf", "T_contrast_names", "T_condition_names", "T_contrast_weights", "sess_cond_durations"))

        # default and initial values
        self.timing_units = 'secs'
        self.interscan_interval = 2.0
        self.sess_cond_names = [['Inc', 'Con'], ['Inc', 'Con']]
        self.sess_cond_onsets = [[[0.0, 10.0, 20.0, 52.0, 88.0, 130.0, 144.0, 174.0, 236.0, 248.0, 260.0, 274.0], [32.0, 42.0, 64.0, 76.0, 102.0, 116.0, 154.0, 164.0, 184.0, 196.0, 208.0, 222.0]], [[0.0, 10.0, 52.0, 64.0, 88.0, 150.0, 164.0, 174.0, 184.0, 196.0, 232.0, 260.0], [20.0, 30.0, 40.0, 76.0, 102.0, 116.0, 130.0, 140.0, 208.0, 220.0, 246.0, 274.0]]]
        self.sess_cond_tmod = [[0, 0], [0, 0]]
        self.sess_cond_orth = [[1, 1], [1, 1]]
        self.sess_hpf = [128.0, 128.0]
        self.T_contrast_names = ['Inc-Con']
        self.T_condition_names = [['Inc', 'Con']]
        self.T_contrast_weights = [[0.5, -0.5, 0.5, -0.05]]
        self.sess_cond_durations = [[[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0], [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]], [[2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0], [2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0, 2.0]]]

        # nodes positions
        self.node_position = {
            "level1design_1": (-760.0, -213.0),
            "estimatemodel_1": (-481.0, 17.0),
            "estimatecontrast_1": (-9.0, 152.0),
            "outputs": (470.4402929185573, 81.0),
            "inputs": (-983.75, 81.0),
        }

        # nodes dimensions
        self.node_dimension = {
            "level1design_1": (376.03125, 880.0),
            "estimatemodel_1": (299.171875, 390.0),
            "estimatecontrast_1": (313.0625, 425.0),
            "outputs": (152.64929503946317, 145.0),
            "inputs": (171.140625, 460.0),
        }

        self.do_autoexport_nodes_parameters = False
