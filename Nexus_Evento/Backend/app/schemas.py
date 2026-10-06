from datetime import date
from decimal import Decimal
from typing import Optional, Literal

from pydantic import BaseModel, Field, EmailStr

class StaffBase(BaseModel):
    nombre: str
    cargo: str
    area: str
    correo: str
    fecha_ingreso: date
    jefe_id: Optional[int] = None


class StaffCreate(StaffBase):
    nombre: str = Field(..., min_length=3, max_length=150)
    cargo: str = Field(..., max_length=100)
    area: Literal["Dirección", "Operaciones", "Comercial", "Logística", "Alimentos y Bebidas", "Audiovisuales"]
    correo: EmailStr


class StaffResponse(StaffBase):
    id: int

    class Config:
        from_attributes = True


class AsistenteBase(BaseModel):
    documento: str
    nombre: str
    correo: str
    empresa: Optional[str] = None


class AsistenteCreate(AsistenteBase):
    documento: str = Field(..., min_length=5, max_length=20)
    nombre: str = Field(..., min_length=3, max_length=150)
    correo: EmailStr
    empresa: Optional[str] = Field(None, max_length=150)


class AsistenteResponse(AsistenteBase):
    id: int

    class Config:
        from_attributes = True