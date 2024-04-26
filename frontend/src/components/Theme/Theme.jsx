import React from 'react';
import { useSelector, useDispatch } from 'react-redux';

import { set } from '../../slices/themeSlice/themeSlice';
import styles from './Theme.module.scss';

const Theme = ({ className }) => {
	const theme = useSelector(state => state.theme);
	const dispatch = useDispatch();

	React.useEffect(() => {
		document.documentElement.dataset.theme = theme;
		localStorage.setItem('theme', theme);
	}, [theme]);

	const handleChange = () => {
		const next = theme === 'dark' ? 'light' : 'dark';
		dispatch(set(next));
	};

	return (
		<label className={styles.switch} htmlFor="checkbox">
			<input id="checkbox" type="checkbox" onClick={handleChange} aria-label="switch" />
			<div className={styles.slider}>
				<span className={styles.icon} />
			</div>
		</label>
	);
};

export default Theme;
