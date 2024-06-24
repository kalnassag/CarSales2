from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship
from typing import List, Optional
from sqlalchemy import DateTime, String, ForeignKey, Integer, Float, Table
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

# Association table for the many-to-many relationship between CarListing and Category
car_listing_category = Table(
    "car_listing_category",
    Base.metadata,
    mapped_column("car_id", ForeignKey("car_listings.car_id"), primary_key=True),
    mapped_column("cat_id", ForeignKey("category.cat_id"), primary_key=True),
)


class User(Base):
    __tablename__ = "user_account"
    user_id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(80))
    email: Mapped[str] = mapped_column(String(80))
    phone_number: Mapped[Optional[str]] = mapped_column(String(80), nullable=True)
    address: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)
    password: Mapped[str] = mapped_column(String(40))

    car_listings: Mapped[List["CarListing"]] = relationship(
        "CarListing", back_populates="user"
    )
    garages: Mapped[List["Garage"]] = relationship("Garage", back_populates="user")
    orders: Mapped[List["Order"]] = relationship("Order", back_populates="user")
    contact_us: Mapped[List["ContactUs"]] = relationship(
        "ContactUs", back_populates="user"
    )


class CarListing(Base):
    __tablename__ = "car_listings"
    car_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"))
    make: Mapped[str] = mapped_column(String(20))
    model: Mapped[str] = mapped_column(String(20))
    year: Mapped[int] = mapped_column(Integer)
    price: Mapped[float] = mapped_column(Float)
    description: Mapped[str] = mapped_column(String(500))
    features: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)
    pictures: Mapped[Optional[str]] = mapped_column(String(100), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="car_listings")
    categories: Mapped[List["Category"]] = relationship(
        "Category", secondary=car_listing_category, back_populates="car_listings"
    )


class Category(Base):
    __tablename__ = "category"
    cat_id: Mapped[int] = mapped_column(primary_key=True)
    category_name: Mapped[str] = mapped_column(String(20))

    car_listings: Mapped[List["CarListing"]] = relationship(
        "CarListing", secondary=car_listing_category, back_populates="categories"
    )


class Garage(Base):
    __tablename__ = "garage"
    garage_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"))

    user: Mapped["User"] = relationship("User", back_populates="garages")


class Order(Base):
    __tablename__ = "orders"
    order_id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"))
    payment_method: Mapped[str] = mapped_column(String(20))
    order_amount: Mapped[float] = mapped_column(Float)
    order_date: Mapped[DateTime] = mapped_column(DateTime)
    billing_address: Mapped[Optional[str]] = mapped_column(String(200), nullable=True)

    user: Mapped["User"] = relationship("User", back_populates="orders")


class ContactUs(Base):
    __tablename__ = "contactus"
    contact_form_id: Mapped[int] = mapped_column(primary_key=True)
    contact_email: Mapped[str] = mapped_column(String(40))
    user_id: Mapped[int] = mapped_column(ForeignKey("user_account.user_id"))
    phone_number: Mapped[Optional[str]] = mapped_column(String(20), nullable=True)
    message: Mapped[str] = mapped_column(String(200))
    submission_date: Mapped[DateTime] = mapped_column(DateTime)

    user: Mapped["User"] = relationship("User", back_populates="contact_us")
