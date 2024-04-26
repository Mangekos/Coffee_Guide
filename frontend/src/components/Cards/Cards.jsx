import { useEffect, useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';
import queryString from 'query-string';

import { setCards, clearCards, setFiltered, clear } from '../../slices/cardsSlice/cardsSlice';
import { useGetCardsQuery } from '../../slices/apiSlice/apiSlice';

import { increment, reset } from '../../slices/offsetSlice/offsetSlice';

import CardSmall from '../CardSmall/CardSmall';
import styles from './Cards.module.scss';
import { set } from '../../slices/themeSlice/themeSlice';

function Cards() {
	const dispatch = useDispatch();
	const card = useSelector(state => state.cards.cards);
	const filters = useSelector(state => state.cards.filters);
	const query = useSelector(state => state.cards.query);
	const offsetCounter = useSelector(state => state.offset);

	const { data, isLoading, isSuccess, isFetching, refetch } = useGetCardsQuery(
		{
			name: query,
			address: query,
			page: offsetCounter,
			availables: queryString.stringify({ availables: [...filters] }),
		},
		{ refetchOnMountOrArgChange: true },
	);

	useEffect(() => {
		if (isSuccess && !query) {
			dispatch(setCards(data.results));
		}
		if (query) {
			dispatch(setFiltered(data.results));
		}
	}, [data]);

	const handleClick = () => {
		dispatch(increment());
	};

	if (isLoading) {
		return <p>loading....</p>;
	}

	console.log(data);

	return (
		<div className={styles.container}>
			<ul>
				{card?.map(card => (
					<li key={card.id}>
						<CardSmall card={card} />
					</li>
				))}
			</ul>
			{data.next !== null && (
				<button type="button" className={styles.more} onClick={handleClick}>
					Показать больше кофеен
				</button>
			)}
		</div>
	);
}

export default Cards;
