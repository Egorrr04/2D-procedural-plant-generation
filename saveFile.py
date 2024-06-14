
import gui


def save_parameters_to_file(filename):
    parameters_to_save = {

        'Size Leaves 1': gui.gui.comboSizeLeaves1.get(),
        'Size Leaves 2': gui.gui.comboSizeLeaves2.get(),
        'Size Leaves 3': gui.gui.comboSizeLeaves3.get(),
        'Size Leaves 4': gui.gui.comboSizeLeaves4.get(),
        'Plant Thickness': gui.gui.comboPlantThickness.get(),
        'Colors Leaf 1': gui.gui.comboColorsLeaf1.get(),
        'Colors Leaf 2': gui.gui.comboColorsLeaf2.get(),
        'Colors Leaf 3': gui.gui.comboColorsLeaf3.get(),
        'Colors Leaf 4': gui.gui.comboColorsLeaf4.get(),
        'Colors Trunk 1': gui.gui.comboColorsTrunk1.get(),
        'Colors Trunk 2': gui.gui.comboColorsTrunk2.get(),
        'Colors Trunk 3': gui.gui.comboColorsTrunk3.get(),
        'Per Leaves 1': gui.gui.comboPerLeaves1.get(),
        'Per Leaves 2': gui.gui.comboPerLeaves2.get(),
        'Per Leaves 3': gui.gui.comboPerLeaves3.get(),
        'Per Leaves 4': gui.gui.comboPerLeaves4.get(),
        'Angle': gui.gui.comboAngle.get(),
        'Segment Length': gui.gui.comboSegmentLength.get(),

        'Generation': gui.gui.comboDepth.get(),
        'Axiom': gui.gui.entry.get(),
        'Rule': gui.gui.text.get('1.0', gui.tk.END),
    }
    with open(filename, 'w') as file:
        for key, value in parameters_to_save.items():
            file.write(f"{key}: {value}\n")
