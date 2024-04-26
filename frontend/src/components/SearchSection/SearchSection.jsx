import { useState, useCallback, useMemo, useEffect } from 'react';
import { useForm } from 'react-hook-form';
import { useNavigate } from 'react-router-dom';
import { useSelector, useDispatch } from 'react-redux';
import {
	setCards,
	clearCards,
	clearFiltered,
	setFiltered,
	setQuery,
	clear,
} from '../../slices/cardsSlice/cardsSlice';
import { useGetCardsQuery } from '../../slices/apiSlice/apiSlice';

// import cn from 'classnames';

import styles from './SearchSection.module.scss';
import Button from '../../assets/ui-kit/Button/Button';
import SearchResult from '../SearchResult/SearchResult';
import { set } from '../../slices/themeSlice/themeSlice';

function SearchSection() {
	const query = useSelector(state => state.cards.query);
	const filtered = useSelector(state => state.cards.filtered);
	const debounce = (func, delay) => {
		let timer;
		return function debounced(...args) {
			clearTimeout(timer);
			timer = setTimeout(() => {
				func(...args);
			}, delay);
		};
	};

	const [inputValue, setInputValue] = useState('');
	const [placeholder, setPlaceholder] = useState('Название кофеӣни / адрес');
	const [isOpen, setIsOpen] = useState(false);

	const dispatch = useDispatch();

	const sendRequest = useCallback(inputValue => {
		dispatch(setQuery(inputValue));
		setIsOpen(true);
	}, []);

	const debouncedSendRequest = useMemo(() => debounce(sendRequest, 1000), [sendRequest]);

	const handleChange = e => {
		const { value } = e.target;
		setInputValue(value);
		dispatch(clearFiltered());
		debouncedSendRequest(value);
	};

	const handleSubmit = e => {
		e.preventDefault();
		dispatch(clearCards());
		dispatch(setCards(filtered));
		setInputValue('');
		setIsOpen(false);
	};

	return (
		<form className={styles.container} onSubmit={e => handleSubmit(e)} noValidate>
			<div className={styles.input_container}>
				<input
					className={styles.input}
					placeholder={placeholder}
					value={inputValue}
					onChange={handleChange}
				/>
				<SearchResult isVisible={isOpen} />
			</div>
			<Button type="submit" text="найти" size="small" disabled={!query} />
		</form>
	);
}

export default SearchSection;
