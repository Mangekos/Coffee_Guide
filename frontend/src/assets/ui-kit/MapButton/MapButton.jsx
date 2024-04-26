import { useState } from 'react';

import cn from 'classnames';
import PropTypes from 'prop-types';
import styles from './MapButton.module.scss';

function MapButton({ type, theme, active, click }) {
	const [isActive, setIsActive] = useState(active);

	const buttonClassName = cn(styles.default);
	const buttonActiveClassName = cn(styles.default, styles.active);

	const handleClick = () => {
		click();
	};

	return (
		<button
			type={type}
			className={isActive ? buttonActiveClassName : buttonClassName}
			onClick={() => {
				setIsActive(!isActive);
				handleClick();
			}}
			aria-label="MapButton"
		/>
	);
}

MapButton.propTypes = {
	type: PropTypes.oneOf(['submit', 'button']),
	theme: PropTypes.oneOf(['light', 'dark']),
	active: PropTypes.bool,
};

MapButton.defaultProps = {
	type: 'button',
	theme: 'light',
	active: false,
};

export default MapButton;
