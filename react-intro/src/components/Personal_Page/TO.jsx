import React, { useState, useEffect } from 'react';
import { fetchMaintenanceData } from './Main_Info';
import {getServiceCompanyName, getMaintenanceTypeName, getMaintenancecarName } from './Utils';

const TO = ({ carId }) => {
    const [maintenanceData, setMaintenanceData] = useState([]);
    const [userCarId, setUserCarId] = useState(null); // Переменная для хранения carId пользователя
    const [allMaintenanceData, setAllMaintenanceData] = useState([]); // Переменная для всех данных ТО

    useEffect(() => {
        const fetchData = async () => {
            setUserCarId(carId); // Устанавливаем carId пользователя
            const data = await fetchMaintenanceData(carId);
            setMaintenanceData(data);
            setAllMaintenanceData(data); // Сохраняем все данные ТО
        };
        fetchData();
    }, [carId]);

    const filteredData = allMaintenanceData.filter(item => item.car === 1);

    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Зав. № машины</th>
                        <th>Вид ТО</th>
                        <th>Дата проведения ТО</th>
                        <th>Наработка, м/час</th>
                        <th>№ заказ-наряда</th>
                        <th>Дата заказ-наряда</th>
                        <th>Организация, проводившая ТО</th>
                    </tr>
                </thead>
                <tbody>
                    {filteredData.map(item => (
                        <tr key={item.id}>
                            <td>{getMaintenancecarName(item.car)}</td>

                            <td>{getMaintenanceTypeName(item.type)}</td>
                            <td>{item.date}</td>
                            <td>{item.operating_time}</td>
                            <td>{item.order_number}</td>
                            <td>{item.order_date}</td>
                            <td>{getServiceCompanyName(item.service_company)}</td>

                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default TO;
