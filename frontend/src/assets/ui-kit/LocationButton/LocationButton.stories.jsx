import LocationButton from './LocationButton';

import '../../../index.scss';

export default {
	title: 'LocationButton',
	tags: ['autodocs'],
	component: LocationButton,
};

export const DefaultLocationButton = {
	args: {
		theme: 'light',
		type: 'button',
		active: false,
	},
};

export const DefaultFLocationButtonActive = {
	args: {
		theme: 'light',
		type: 'button',
		active: true,
	},
};
