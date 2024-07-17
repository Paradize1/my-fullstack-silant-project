// login.js
import { useState, useContext } from 'react';
import { useNavigate } from 'react-router-dom';
import { AuthContext } from '../services/AuthContext';

const useLogin = () => {
    const [error, setError] = useState('');
    const navigate = useNavigate();
    const { login, logout } = useContext(AuthContext);

    const handleLogin = async (username, password) => {
        try {
            const response = await fetch('http://127.0.0.1:8000/api/login/', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ username, password }),
            });

            const data = await response.json();

            if (response.ok) {
                if (data && data.id) {
                    localStorage.setItem('isAuthenticated', 'true');
                    localStorage.setItem('username', username);
                    localStorage.setItem('userId', data.id);
                    localStorage.setItem('username_display', data.username_display);
                    localStorage.setItem('usernameStatus', data.status);

                    login(data.username_display, data.id, data.status); // Вызов функции login с username_display и status
                    navigate('/Personal_Page');
                } else {
                    setError('Server response does not contain user profile id');
                }
            } else {
                setError(data.error || 'Something went wrong');
            }
        } catch (error) {
            setError('Error during request execution');
        }
    };

    const handleLogout = () => {
        logout();
        navigate('/');
    };

    return { error, login: handleLogin, logout: handleLogout };
};

export default useLogin;



