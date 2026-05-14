from pydantic import BaseModel, EmailStr, Field
from typing import Optional

class UsuarioSchema(BaseModel):
    nombre: str = Field(min_length=3, max_length=100)
    apellido: str = Field(min_length=3, max_length=100)
    # Usamos default=None para mayor claridad en v2
    telefono: Optional[str] = Field(default=None, max_length=20)
    email: EmailStr
    password: str = Field(min_length=6)