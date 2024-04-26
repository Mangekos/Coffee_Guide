import { useSelector, useDispatch } from 'react-redux';
import { Link, useNavigate } from 'react-router-dom';
import cn from 'classnames';

import styles from './SearchResult.module.scss';

function SearchResult({ isVisible }) {
	const navigate = useNavigate();
	const cards = useSelector(state => state.cards.filtered);

	const handleClick = card => {
		navigate(`/card/${card.id}`, { state: { key: card.id } });
	};

	const resultClassName = cn(
		styles.result_container,
		isVisible ? styles.popup_opened : styles.popup,
	);

	return (
		<div className={resultClassName}>
			<ul className={styles.result}>
				{cards?.slice(0, 4).map(item => (
					<li onClick={() => handleClick(item)} className={styles.item} key={item.id}>
						<p className={styles.title}>{item.name}</p>
						<address className={styles.address}>{item.address.name}</address>
					</li>
				))}
			</ul>
		</div>
	);
}

export default SearchResult;
