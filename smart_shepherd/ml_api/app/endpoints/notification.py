from fastapi import APIRouter, Body


notif_router=APIRouter(tags=["Notification of Type Animal"])

@notif_router.post("/notification")
def get_notification(data :dict = Body(...)):
	return data
