def car_basicinfo(brand,model,**car_infos):
    car_infos['brand']=brand
    car_infos['model']=model
    return car_infos

car_info=car_basicinfo('tesla','model3',color='blue',tow_package=False)

print(car_info)