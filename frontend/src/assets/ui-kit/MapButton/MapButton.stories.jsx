import MapButton from './MapButton';

import '../../../index.scss';

export default {
	title: 'MapButton',
	tags: ['autodocs'],
	component: MapButton,
};

export const OpenMapButton = {
	args: {
		theme: 'light',
		type: 'button',
		active: false,
	},
};

export const CloseMapButton = {
	args: {
		theme: 'light',
		type: 'button',
		active: true,
	},
};
