from simple_folder_launcher import check_path_exists, get_users_document_folder


def test_check_path_exists_success():
    exists = check_path_exists("c:")
    assert exists == True


def test_check_path_exists_failure():
    exists = check_path_exists("notletterdrive:")
    assert exists == False


def test_get_users_document_folder():
    pass
    document_folder_path = get_users_document_folder()
    assert document_folder_path != None
    assert "\\Documents" in document_folder_path
