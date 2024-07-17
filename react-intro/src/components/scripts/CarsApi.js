export const fetchCars = async () => {
  try {
    console.log('Поиск по API пошёл');
    const response = await fetch('http://127.0.0.1:8000/api/cars/');
    if (!response.ok) {
      throw new Error('Ошибка сети');
    }
    const data = await response.json();
    console.log('Полученная информация:', data);
    return data;
  } catch (error) {
    console.error('Ошибка при запросе:', error);
    return [];
  }
};