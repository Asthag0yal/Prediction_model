from fastapi import APIRouter, Depends
from pydantic import BaseModel
from app.core.dependencies import get_api_key, get_current_user
from app.services.model_service import predict_car_price

router = APIRouter()


class CarFeatures(BaseModel):
    name: str
    year: int
    selling_price: int
    km_driven: int
    fuel: str
    seller_type: str
    transmission: str
    owner: str
    mileage: float
    engine: float
    max_power: float
    torque: float
    seats: float

    @router.post('/predict')
    def predict_price(car: CarFeatures, user=Depends(get_current_user),_=Depends(get_api_key)):
        prediction = predict_car_price(car.model_dump())
        return {'predicted_price': f'{prediction:,.2f}'}

