// GeneralInfo.jsx

import React, { useState, useEffect, useContext } from 'react';
import { AuthContext } from '../services/AuthContext';
import { fetchCarById } from './Main_Info';
import { getServiceCompanyName } from './Utils';



const GeneralInfo = () => {
  const { getUserData } = useContext(AuthContext);
  const [carData, setCarData] = useState(null);

  useEffect(() => {
    async function fetchCarData() {
      const userData = getUserData();

      if (userData && userData.userId) {
        try {
          console.log('Fetching car data for userId:', userData.userId); // Лог для проверки userId
          const data = await fetchCarById(userData.userId);
          setCarData(data);
        } catch (error) {
          console.error('Ошибка при загрузке данных о машине:', error);
        }
      }
    }

    fetchCarData();
  }, [getUserData]);

  if (!carData) {
    return <div>Нет данных для отображения</div>;
  }




  return (
    <div className='body_table'>
      <table>
        <thead>
          <tr>
            <th>Заводской номер</th>
            <th>Модель техники</th>
            <th>Модель двигателя</th>
            <th>Зав. № двигателя</th>
            <th>Модель трансмиссии</th>
            <th>Зав. № трансмиссии</th>
            <th>Модель ведущего моста</th>
            <th>Зав. № ведущего моста</th>
            <th>Модель управляемого моста</th>
            <th>Зав. № управляемого моста</th>
            <th>Грузополучатель (конечный потребитель)</th>
            <th>Адрес поставки (эксплуатации)</th>
            <th>Комплектация (доп. опции)</th>
            <th>Сервисная компания</th>
          </tr>
        </thead>
        <tbody>
          <tr key={carData.id}>
            <td>{carData.car_number}</td>
            <td>{carData.technic_name}</td>
            <td>{carData.engine_name}</td>
            <td>{carData.engine_number}</td>
            <td>{carData.transmission_name}</td>
            <td>{carData.transmission_number}</td>
            <td>{carData.driving_bridge_name}</td>
            <td>{carData.driving_bridge_number}</td>
            <td>{carData.controlled_bridge_name}</td>
            <td>{carData.controlled_bridge_number}</td>
            <td>{carData.consignee}</td>
            <td>{carData.delivery_address}</td>
            <td>{carData.equipment}</td>
            <td>{getServiceCompanyName(carData.service_company)}</td>
          </tr>
        </tbody>
      </table>
    </div>
  );
};

export default GeneralInfo;




