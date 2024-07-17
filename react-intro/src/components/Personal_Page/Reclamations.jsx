// Reclamations.jsx

import React, { useState, useEffect } from 'react';
import { fetchReclamationsData } from './Main_Info';
import {getMaintenancecarName, getrecoverymethodName } from './Utils';

const Reclamations = ({ carId }) => {
    const [reclamationsData, setReclamationsData] = useState([]);

    useEffect(() => {
        const fetchData = async () => {
            const data = await fetchReclamationsData(carId);
            setReclamationsData(data);
            console.log('all: ', data)

           

        };
        fetchData();
    }, [carId]);


    const filteredReclamations = reclamationsData.filter(item => item.car === 1);
    console.log('фильтр: ', filteredReclamations)

    return (
        <div>
            <table>
                <thead>
                    <tr>
                        <th>Зав. № машины</th>
                        <th>Дата отказа</th>
                        <th>Наработка, м/час</th>
                        <th>Узел отказа</th>
                        <th>Описание отказа</th>
                        <th>Способ восстановления</th>
                        <th>Используемые запасные части</th>
                        <th>Дата восстановления</th>
                        <th>Время простоя техники</th>
                    </tr>
                </thead>
                <tbody>
                    {filteredReclamations.map(item => (
                        <tr key={item.id}>
                            <td>{getMaintenancecarName(item.car)}</td>
                            <td>{item.date_failure}</td>
                            <td>{item.operating_time}</td>
                            <td>{item.node_failure}</td>
                            <td>{item.description_failure}</td>
                            <td>{getrecoverymethodName(item.method_recovery)}</td>

                            <td>{item.repair_parts}</td>
                            <td>{item.date_recovery}</td>
                            <td>{item.time}</td>
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default Reclamations;



