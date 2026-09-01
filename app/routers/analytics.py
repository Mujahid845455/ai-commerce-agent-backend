from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from sqlalchemy import func, desc

from app.core.database import get_db
from app.core.auth import get_current_user
from app.models.order import Order, OrderItem
from app.models.product import Product
from app.models.audit import AuditLog


router = APIRouter(
    prefix="/analytics",
    tags=["Analytics"]
)


@router.get("/overview")
def get_analytics_overview(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Returns high-level analytics for the merchant dashboard.

    Includes:
    - Total orders (all statuses)
    - Confirmed/paid orders
    - Total revenue (paise)
    - Average order value (paise)
    - Payment success rate
    - Payment failure count
    """

    # ------------------------------------------------
    # Total orders
    # ------------------------------------------------
    total_orders = (
        db.query(func.count(Order.id))
        .scalar()
        or 0
    )

    # ------------------------------------------------
    # Confirmed (paid) orders
    # ------------------------------------------------
    confirmed_orders = (
        db.query(func.count(Order.id))
        .filter(Order.status == "CONFIRMED")
        .scalar()
        or 0
    )

    # ------------------------------------------------
    # Failed payments
    # ------------------------------------------------
    failed_payments = (
        db.query(func.count(Order.id))
        .filter(Order.payment_status == "FAILED")
        .scalar()
        or 0
    )

    # ------------------------------------------------
    # Pending orders
    # ------------------------------------------------
    pending_orders = (
        db.query(func.count(Order.id))
        .filter(Order.status == "PENDING")
        .scalar()
        or 0
    )

    # ------------------------------------------------
    # Total revenue (from CONFIRMED orders only)
    # ------------------------------------------------
    total_revenue_paise = (
        db.query(
            func.sum(Order.total_amount_paise)
        )
        .filter(Order.status == "CONFIRMED")
        .scalar()
        or 0
    )

    # ------------------------------------------------
    # Average order value
    # ------------------------------------------------
    avg_order_value_paise = (
        round(total_revenue_paise / confirmed_orders)
        if confirmed_orders > 0
        else 0
    )

    # ------------------------------------------------
    # Payment success rate
    # ------------------------------------------------
    payment_success_rate = (
        round(
            (confirmed_orders / total_orders) * 100, 1
        )
        if total_orders > 0
        else 0.0
    )

    # ------------------------------------------------
    # Total products
    # ------------------------------------------------
    total_products = (
        db.query(func.count(Product.id))
        .filter(Product.is_active == True)
        .scalar()
        or 0
    )

    # ------------------------------------------------
    # Low stock products (stock <= 5)
    # ------------------------------------------------
    low_stock_count = (
        db.query(func.count(Product.id))
        .filter(
            Product.is_active == True,
            Product.stock_quantity <= 5,
            Product.stock_quantity > 0,
        )
        .scalar()
        or 0
    )

    # ------------------------------------------------
    # Out of stock products
    # ------------------------------------------------
    out_of_stock_count = (
        db.query(func.count(Product.id))
        .filter(
            Product.is_active == True,
            Product.stock_quantity == 0,
        )
        .scalar()
        or 0
    )

    return {
        "total_orders": total_orders,
        "confirmed_orders": confirmed_orders,
        "pending_orders": pending_orders,
        "failed_payments": failed_payments,
        "total_revenue_paise": total_revenue_paise,
        "total_revenue_inr": round(
            total_revenue_paise / 100, 2
        ),
        "avg_order_value_paise": avg_order_value_paise,
        "avg_order_value_inr": round(
            avg_order_value_paise / 100, 2
        ),
        "payment_success_rate": payment_success_rate,
        "total_products": total_products,
        "low_stock_count": low_stock_count,
        "out_of_stock_count": out_of_stock_count,
    }


@router.get("/orders")
def get_recent_orders(
    limit: int = 20,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Returns the most recent orders for the merchant dashboard.
    """

    orders = (
        db.query(Order)
        .order_by(desc(Order.created_at))
        .limit(limit)
        .all()
    )

    result = []

    for order in orders:

        # Load items for this order
        items = (
            db.query(OrderItem)
            .filter(OrderItem.order_id == order.id)
            .all()
        )

        result.append({
            "id": str(order.id),
            "user_id": str(order.user_id),
            "status": order.status,
            "payment_status": order.payment_status,
            "total_amount_paise": order.total_amount_paise,
            "total_amount_inr": round(
                order.total_amount_paise / 100, 2
            ),
            "currency": order.currency,
            "razorpay_order_id": order.razorpay_order_id,
            "razorpay_payment_id": order.razorpay_payment_id,
            "created_at": str(order.created_at),
            "items": [
                {
                    "product_id": str(item.product_id),
                    "product_name": item.product_name,
                    "quantity": item.quantity,
                    "unit_price_paise": item.unit_price_paise,
                    "unit_price_inr": round(
                        item.unit_price_paise / 100, 2
                    ),
                    "total_price_paise": item.total_price_paise,
                    "total_price_inr": round(
                        item.total_price_paise / 100, 2
                    ),
                }
                for item in items
            ],
        })

    return result


@router.get("/audit")
def get_audit_logs(
    limit: int = 50,
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Returns audit log entries for the merchant dashboard.
    Shows all recorded payment/order actions with their status.
    """

    logs = (
        db.query(AuditLog)
        .order_by(desc(AuditLog.created_at))
        .limit(limit)
        .all()
    )

    return [
        {
            "id": str(log.id),
            "action": log.action,
            "status": log.status,
            "product_id": str(log.product_id) if log.product_id else None,
            "amount_paise": log.amount_paise,
            "amount_inr": round(
                log.amount_paise / 100, 2
            ) if log.amount_paise else None,
            "details": log.details,
            "created_at": str(log.created_at),
        }
        for log in logs
    ]


@router.get("/revenue")
def get_revenue_breakdown(
    db: Session = Depends(get_db),
    current_user=Depends(get_current_user),
):
    """
    Returns revenue breakdown by product for the merchant dashboard.
    Shows which products have generated the most revenue.
    """

    # Get revenue by product from confirmed orders
    revenue_by_product = (
        db.query(
            OrderItem.product_id,
            OrderItem.product_name,
            func.sum(OrderItem.total_price_paise).label("total_revenue_paise"),
            func.sum(OrderItem.quantity).label("units_sold"),
            func.count(OrderItem.id).label("order_count"),
        )
        .join(
            Order,
            Order.id == OrderItem.order_id
        )
        .filter(Order.status == "CONFIRMED")
        .group_by(
            OrderItem.product_id,
            OrderItem.product_name
        )
        .order_by(
            desc("total_revenue_paise")
        )
        .limit(20)
        .all()
    )

    return [
        {
            "product_id": str(row.product_id),
            "product_name": row.product_name,
            "total_revenue_paise": row.total_revenue_paise,
            "total_revenue_inr": round(
                row.total_revenue_paise / 100, 2
            ),
            "units_sold": row.units_sold,
            "order_count": row.order_count,
        }
        for row in revenue_by_product
    ]
