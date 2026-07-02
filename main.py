"""
- phân tích:
input: order_id: int
output: 200 OK, 404 Not Found,500 Internal Server Error
- giải pháp:
Giải pháp 1: Lưu dữ liệu dạng List và cách duyệt mảng để tìm kiếm.
Giải pháp 2: Lưu dữ liệu dạng Dict và cách tra cứu trực tiếp qua Key.
- so sánh:
list: chậm, code it hơn, dẽ hiểu, bảo trì chưa tốt, không phù hợp dữ liệu lớn
dict: nhanh, nhiều code, dễ hiểu, bảo trì tốt, phù hợp dữ liệu nhiều
- chọn dict: tra cứu nhanh,order_id là khóa duy nhất, nhiều đơn hàng.
"""
from fastapi import FastAPI, HTTPException, status
app = FastAPI()
orders_dict = {
    1: {"id": 1, "code": "SP001", "payment_status": "PAID", "method": "BANK_TRANSFER"},
    2: {"id": 2, "code": "SP002", "payment_status": "UNPAID", "method": "NONE"}
}
@app.get("/orders/{order_id}/payment")
def get_payment(order_id: int):
    try:
        order = orders_dict.get(order_id)
        if not order:
            raise HTTPException(
                status_code=status.HTTP_404_NOT_FOUND,
                detail="Order not found"
            )
        return {
            "payment_status": order["payment_status"],
            "method": order["method"]
        }
    except HTTPException:
        raise
    except Exception:
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="Đã xảy ra lỗi hệ thống. Vui lòng thử lại sau."
        )