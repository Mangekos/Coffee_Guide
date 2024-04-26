import FavouritesButton from './FavouritesButton';

import '../../../index.scss';

export default {
	title: 'FavouritesButton',
	tags: ['autodocs'],
	component: FavouritesButton,
};

export const DefaultFavouritesButton = {
	args: {
		theme: 'light',
		type: 'button',
		active: false,
	},
};

export const DefaultFavouritesButtonActive = {
	args: {
		theme: 'light',
		type: 'button',
		active: true,
	},
};
