import { useState } from 'react';
import { useSelector } from 'react-redux';

import cn from 'classnames';
import PropTypes from 'prop-types';
import styles from './TagButton.module.scss';

import { TAG_ICONS } from './TagIcons';

function TagButton({ text, type, theme, tag, active, onClick }) {
	const [isActive, setIsActive] = useState(active);
	const { light, dark } = TAG_ICONS[tag];

	const btnClassName = cn(styles.button, { [styles.checked]: isActive });
	const textClassName = cn(styles.text);

	const handleClick = () => {
		setIsActive(!isActive);
		onClick();
	};

	return (
		<button type={type} className={btnClassName} onClick={() => handleClick(tag)}>
			{theme === 'light' ? (
				<img src={light} className={styles.icon} alt="icon" />
			) : (
				<img src={dark} className={styles.icon} alt="icon" />
			)}
			<p className={textClassName}>{text}</p>
		</button>
	);
}

TagButton.propTypes = {
	type: PropTypes.oneOf(['submit', 'button']),
	// theme: PropTypes.oneOf(['light', 'dark']),
	tag: PropTypes.oneOf(['alternative', 'submarine', 'lactose_free_milk', 'la_marzocco', 'sweater']),
	active: PropTypes.bool,
};

TagButton.defaultProps = {
	type: 'button',
	// theme: 'light',
	tag: 'alternative',
	active: false,
};

export default TagButton;
