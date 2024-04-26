import { useEffect, useState } from 'react';
import { useSelector } from 'react-redux';
import BackButton from '../../assets/ui-kit/BackButton/BackButton';
import CardSmall from '../CardSmall/CardSmall';
import styles from './Favourites.module.scss';

function Favourites() {
	const theme = useSelector(state => state.theme);
	const saved = useSelector(state => state.cards.favourites);

	return (
		<section className={styles.container}>
			<div className={styles.back_button}>
				<BackButton type="button" theme={theme} text="Назад" />
			</div>
			{saved.length === 0 && (
				<div className={styles.no_favourites}>
					<p className={styles.text}>В избранном пока ничего нет.</p>
					<div className={theme === 'light' ? styles.coffee_cup : styles.coffee_cup_dark} />
				</div>
			)}

			<div className={styles.cardlist}>
				<ul>
					{saved.map(item => (
						<li key={item.id}>
							<CardSmall card={item} />
						</li>
					))}
				</ul>
			</div>
		</section>
	);
}

export default Favourites;
