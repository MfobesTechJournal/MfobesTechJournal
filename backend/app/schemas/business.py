from pydantic import BaseModel, ConfigDict


class BusinessBase(BaseModel):
    name: str
    address: str | None = None
    phone: str | None = None
    website: str | None = None


class BusinessCreate(BusinessBase):
    pass


class BusinessRead(BusinessBase):
    id: int

    model_config = ConfigDict(from_attributes=True)
