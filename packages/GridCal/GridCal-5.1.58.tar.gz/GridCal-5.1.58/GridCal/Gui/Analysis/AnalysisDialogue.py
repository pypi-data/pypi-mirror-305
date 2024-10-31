# GridCal
# Copyright (C) 2015 - 2024 Santiago Peñate Vera
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 3 of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin Street, Fifth Floor, Boston, MA  02110-1301, USA.

from typing import List
from PySide6 import QtWidgets
from GridCal.Gui.Analysis.gui import Ui_MainWindow
from GridCal.Gui.Analysis.object_plot_analysis import grid_analysis, GridErrorLog, FixableErrorOutOfRange
from GridCalEngine.Devices.multi_circuit import MultiCircuit
from GridCal.Gui.general_dialogues import LogsDialogue, Logger


class GridAnalysisGUI(QtWidgets.QMainWindow):
    """
    GridAnalysisGUI
    """
    def __init__(self, circuit: MultiCircuit):
        """

        :param circuit: MultiCircuit
        """
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.setWindowTitle('Grid analysis')

        # set the circuit
        self.circuit = circuit

        self.object_types = [dev.device_type.value for dev in circuit.get_template_objects_list()]

        # declare logs
        self.log = GridErrorLog()

        self.fixable_errors: List[FixableErrorOutOfRange] = []

        self.ui.actionSave_diagnostic.triggered.connect(self.save_diagnostic)
        self.ui.actionAnalyze.triggered.connect(self.analyze_all)
        self.ui.actionFix_issues.triggered.connect(self.fix_all)

        self.analyze_all()

    def analyze_all(self):
        """
        Analyze the model data
        :return:
        """
        self.log = GridErrorLog()

        # declare logs
        self.fixable_errors = grid_analysis(
            circuit=self.circuit,
            analyze_ts=self.ui.fixTimeSeriesCheckBox.isChecked(),
            imbalance_threshold=self.ui.activePowerImbalanceSpinBox.value() / 100.0,
            v_low=self.ui.genVsetMinSpinBox.value(),
            v_high=self.ui.genVsetMaxSpinBox.value(),
            tap_min=self.ui.transformerTapModuleMinSpinBox.value(),
            tap_max=self.ui.transformerTapModuleMaxSpinBox.value(),
            transformer_virtual_tap_tolerance=self.ui.virtualTapToleranceSpinBox.value() / 100.0,
            branch_connection_voltage_tolerance=self.ui.lineNominalVoltageToleranceSpinBox.value() / 100.0,
            min_vcc=self.ui.transformerVccMinSpinBox.value(),
            max_vcc=self.ui.transformerVccMaxSpinBox.value(),
            branch_x_threshold=1e-4,
            condition_number_thrshold=1e-4,
            logger=self.log
        )

        # set logs
        self.ui.logsTreeView.setModel(self.log.get_model())

    def fix_all(self):
        """
        Fix all detected fixable errors
        :return:
        """
        logger = Logger()
        for fixable_err in self.fixable_errors:
            fixable_err.fix(logger=logger,
                            fix_ts=self.ui.fixTimeSeriesCheckBox.isChecked())

        if len(logger) > 0:
            dlg = LogsDialogue("Fixed issues", logger)
            dlg.setModal(True)
            dlg.exec_()

        # re-analyze
        self.analyze_all()

    def save_diagnostic(self):
        """
        save_diagnostic
        :return:
        """
        files_types = "Excel (*.xlsx)"

        fname = 'Grid error analysis.xlsx'

        filename, _ = QtWidgets.QFileDialog.getSaveFileName(self, 'Save file', fname, files_types)

        if filename != '':
            self.log.save(filename)
