import React, { useEffect, useState } from 'react';

import { fetchCars } from '../scripts/CarsApi';

import "./Body.css";




function Body() {
  const [cars, setCars] = useState([]);

  const [searchTerm, setSearchTerm] = useState('');
  const [filteredCars, setFilteredCars] = useState([]);
  const [noResults, setNoResults] = useState(false);


  useEffect(() => {
    const getCars = async () => {
      try {
        const data = await fetchCars();
        console.log('Полученные данные:', data);
        setCars(data);  
        setFilteredCars(data); // Инициализируем фильтрованные данные сразу после загрузки
      } catch (error) {
        console.error('Ошибка при загрузке данных:', error);
      }
    };

    getCars();
  }, []);
  
  const handleSearch = () => {
    const filtered = cars.filter(car => car.car_number.includes(searchTerm));
    setFilteredCars(filtered);
    if (filtered.length === 0) {
      setNoResults(true); // Показываем сообщение о пустом результате
    } else {
      setNoResults(false);
    }
  };

  const handleChange = (e) => {
    setSearchTerm(e.target.value);
  };

  const handleKeyDown = (e) => {
    if (e.key === 'Enter') {
      handleSearch();
    }
  };


  return (
    <div className='body'>

        <div className='body_1'>Проверьте комплектацию и технические характеристики <br />техники Силант</div>

        <div className='body_2'>
            <div className='factory_number'>Заводской номер
                <div className='factory_number_input_block'>
                    <input type='text' 
                    className='factory_number_input' 
                    placeholder='Введите номер' 
                    value={searchTerm}
                    onChange={handleChange}
                    onKeyDown={handleKeyDown}/>
                </div>            
            </div>
            <button className='factory_number_search_button'onClick={handleSearch}>Поиск</button>
        </div>

        



        <div className='body_4'>
        {noResults && <p>Ничего не найдено по запросу "{searchTerm}"</p>}
        {!noResults && (
          <div>
            Информация о комплектации и технических<br /> характеристиках техники
          </div>
        )}
      </div>


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
            </tr>
          </thead>
          <tbody>

            {filteredCars.map(car => (
              <tr key={car.id}>

                <td>{car.car_number}</td>
                <td>{car.technic_name}</td>
                <td>{car.engine_name}</td>
                <td>{car.engine_number}</td>
                <td>{car.transmission_name}</td>
                <td>{car.transmission_number}</td>
                <td>{car.driving_bridge_name}</td>
                <td>{car.driving_bridge_number}</td>
                <td>{car.controlled_bridge_name}</td>
                <td>{car.controlled_bridge_number}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}


export default Body;