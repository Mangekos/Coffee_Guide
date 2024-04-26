import { useState } from 'react';

import cn from 'classnames';
import PropTypes from 'prop-types';
import styles from './CheckBox.module.scss';

function CheckBox({ type, theme, active, text }) {
	const [isActive, setIsActive] = useState(active);

	return (
		<label className={styles.label}>
			<input type={type} className={styles.checkbox} aria-label="CheckBox" />
			<p className={styles.text}>{text}</p>
		</label>
	);
}

CheckBox.propTypes = {
	type: PropTypes.oneOf(['checkbox']),
	theme: PropTypes.oneOf(['light', 'dark']),
	active: PropTypes.bool,
};

CheckBox.defaultProps = {
	type: 'checkbox',
	theme: 'light',
	active: false,
};

export default CheckBox;
