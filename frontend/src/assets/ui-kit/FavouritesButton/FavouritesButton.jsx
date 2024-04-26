import { useState } from 'react';
import { useSelector, useDispatch } from 'react-redux';

import cn from 'classnames';
import PropTypes from 'prop-types';
import styles from './FavouritesButton.module.scss';

import { addToFavourite } from '../../../slices/cardsSlice/cardsSlice';

function FavouritesButton({ type, theme, active, onClick, card }) {
	const savedCard = useSelector(state => state.cards.favourites);
	const isLiked = savedCard.some(i => i.id === card.id);

	const buttonClassName = cn(styles.default, { [styles.active]: isLiked });
	const dispatch = useDispatch();
	return (
		<button
			type={type}
			className={buttonClassName}
			onClick={() => dispatch(addToFavourite(card))}
			aria-label="FavouritesButton"
		/>
	);
}

FavouritesButton.propTypes = {
	type: PropTypes.oneOf(['submit', 'button']),
	theme: PropTypes.oneOf(['light', 'dark']),
	active: PropTypes.bool,
};

FavouritesButton.defaultProps = {
	type: 'button',
	theme: 'light',
	active: false,
};

export default FavouritesButton;
