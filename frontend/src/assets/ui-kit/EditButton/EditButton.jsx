// import { useState } from 'react';

import cn from 'classnames';
import PropTypes from 'prop-types';
import styles from './EditButton.module.scss';

function EditButton({ size, theme }) {
	// const [isEdit, setIsEdit] = useState(false);
	const buttonClassName = cn(styles.default, styles[size]);

	return (
		<button
			type="button"
			className={buttonClassName}
			// onClick={() => setIsEdit(true)}
			aria-label="EditButton"
		/>
	);
}

EditButton.propTypes = {
	size: PropTypes.oneOf(['default', 'small']),
	theme: PropTypes.oneOf(['light', 'dark']),
};

EditButton.defaultProps = {
	size: PropTypes.oneOf(['default']),
	theme: 'light',
};

export default EditButton;
