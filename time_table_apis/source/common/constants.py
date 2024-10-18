
success_msg = "Job Done!"
fail_msg = "Some thing went wrong!"
GOOD_JSON = {
    "status_code":200,
    "message":f"SUCCESS,{success_msg}"
}
ERROR_JSON = {
    "status_code":400,
    "message":f"FAILED,{fail_msg}"
}