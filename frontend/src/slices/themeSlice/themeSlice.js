import { createSlice } from '@reduxjs/toolkit';

const getTheme = () => {
	// пытаемся получить тему из локального хранилища браузера
	const theme = `${window?.localStorage?.getItem('theme')}`;
	if (['light', 'dark'].includes(theme)) return theme;

	// если там ничего нет, то пробуем получить тему из настроек системы
	const userMedia = window.matchMedia('(prefers-color-scheme: light)');
	if (userMedia.matches) return 'light';

	// если и настроек нет, то используем темную тему
	return 'dark';
};

const initialState = getTheme();

export const themeSlice = createSlice({
	name: 'theme',
	initialState,
	reducers: {
		set: (state, action) => action.payload,
	},
});

export const { set } = themeSlice.actions;

export default themeSlice.reducer;
