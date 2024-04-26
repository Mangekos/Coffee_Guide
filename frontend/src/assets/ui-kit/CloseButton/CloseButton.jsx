// import { useState } from 'react';

import cn from 'classnames';
import PropTypes from 'prop-types';
import styles from './CloseButton.module.scss';

function CloseButton({ size, theme, onClick }) {
	// const [isOpen, setIsOpen] = useState(true);
	const buttonClassName = cn(styles.default, styles[size]);

	return (
		<button type="button" className={buttonClassName} onClick={onClick} aria-label="CloseButton" />
	);
}

CloseButton.propTypes = {
	size: PropTypes.oneOf(['default', 'small']),
	theme: PropTypes.oneOf(['light', 'dark']),
};

CloseButton.defaultProps = {
	size: PropTypes.oneOf(['default']),
	theme: 'light',
};

export default CloseButton;
