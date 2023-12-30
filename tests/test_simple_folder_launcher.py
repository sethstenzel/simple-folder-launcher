from simple_folder_launcher import check_path_exists


def test_check_path_exsists():
    exists = check_path_exists("c:")
    assert exists == True
    exists = check_path_exists("notletterdrive:")
    assert exists == False
