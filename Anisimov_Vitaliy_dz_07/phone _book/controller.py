import view
import model_csv_file
import model_xml_file
import model_txt_file


def selection_processing():
    selection = view.user_selection()
    if selection == 1:
        import_processing_csv(view.user_data_entry())
    elif selection == 2:
        export_processing_csv()
    elif selection == 3:
        import_processing_xml(view.user_data_entry())
    elif selection == 4:
        export_processing_xml()
    elif selection == 5:
        import_processing_txt(view.user_data_entry())
    elif selection == 6:
        export_processing_txt()


def import_processing_csv(data):
    model_csv_file.file_recording(data)


def export_processing_csv():
    view.view_result(model_csv_file.file_reading())


def import_processing_xml(data):
    model_xml_file.file_recording(data)


def export_processing_xml():
    view.view_result(model_xml_file.file_reading())


def import_processing_txt(data):
    model_txt_file.file_writing(data)


def export_processing_txt():
    view.view_result(model_txt_file.file_reading())