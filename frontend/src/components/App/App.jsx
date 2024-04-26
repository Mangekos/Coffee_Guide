import React, { useState, useEffect } from 'react';
import { Routes, Route, useLocation } from 'react-router-dom';

import ProtectedRoute from '../ProtectedRoute/ProtectedRoute';
import Header from '../Header/Header';
import Main from '../Main/Main';
import Login from '../Login/Login';
import Footer from '../Footer/Footer';
import CardMedium from '../CardMedium/CardMedium';
import Favourites from '../Favourites/Favourites';
import NotFound from '../NotFound/NotFound';
import Register from '../Register/Register';
import Profile from '../Profile/Profile';

import styles from './App.module.scss';

function App() {
	const [loggedIn, setLoggedIn] = useState(!!localStorage.token);

	const tokenCheck = () => {
		if (localStorage.token) {
			setLoggedIn(true);
		}
	};

	useEffect(() => {
		tokenCheck();
	}, []);

	return (
		<div className={styles.root}>
			<Header />
			<Routes>
				<Route path="/" element={<Main />} />
				<Route path="/card/:cardId" element={<CardMedium />} />
				<Route path="/signin" element={<Login />} />
				<Route path="/signup" element={<Register />} />

				<Route path="/favourites" element={<Favourites />} />

				<Route path="/profile" element={<ProtectedRoute element={Profile} loggedIn={loggedIn} />} />

				<Route path="*" element={<NotFound />} />
			</Routes>
			<Footer />
		</div>
	);
}

export default App;
