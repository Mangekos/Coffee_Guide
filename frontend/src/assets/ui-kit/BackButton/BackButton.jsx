import { useNavigate } from 'react-router-dom';
import styles from './BackButton.module.scss';
import lightIcon from '../../images/back.svg';
import darkIcon from '../../images/back-dark.svg';

function BackButton({ type, theme, text }) {
	const navigate = useNavigate();
	const goBack = () => navigate(-1);

	return (
		<button className={styles.back} onClick={goBack} type={type}>
			<img
				src={theme === 'light' ? lightIcon : darkIcon}
				className={styles.back_icon}
				alt="назад"
			/>
			{text}
		</button>
	);
}

export default BackButton;
