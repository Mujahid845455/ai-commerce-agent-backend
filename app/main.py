from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from app.core.database import Base, engine
from app.routers.checkout import router as checkout_router
from app.routers.payment import router as payment_router
from app.routers.analytics import router as analytics_router
from app.models import (
    User,
    Merchant,
    Product,
    Cart,
    CartItem,
    Order,
    OrderItem,
    AuditLog,
)

from app.routers import (
    auth,
    products,
    merchants,
    catalog,
    cart,
    orders,
    conversations,
)


# Create database tables
Base.metadata.create_all(
    bind=engine
)

# Auto-seed catalog on startup
try:
    from seed import seed_database
    seed_database()
except Exception as e:
    print(f"[*] Startup database seed notice: {e}")


app = FastAPI(
    title="AgentPay API",
    description="AI-powered agentic commerce backend",
    version="1.0.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Register routers
app.include_router(auth.router)
app.include_router(products.router)
app.include_router(merchants.router)
app.include_router(catalog.router)
app.include_router(
    cart.router
)
app.include_router(orders.router)
app.include_router(
    checkout_router
)
app.include_router(payment_router)
app.include_router(analytics_router)
app.include_router(conversations.router)



@app.get("/")
def root():

    return {
        "message": "AgentPay API is running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }