import { Link, useLocation } from 'react-router-dom';
import { useDispatch, useSelector } from 'react-redux';
import { clearCards, clearFiltered } from '../../slices/cardsSlice/cardsSlice';

import logo from '../../assets/images/logo.svg';
import logoDark from '../../assets/images/logo-dark.svg';
import icon from '../../assets/images/profile-icon.svg';
import iconDark from '../../assets/images/profile-icon-dark.svg';
import Theme from '../Theme/Theme';
import SearchSection from '../SearchSection/SearchSection';

import styles from './Header.module.scss';

const FullRenderedSection = () => {
	const theme = useSelector(state => state.theme);

	return (
		<>
			<SearchSection />
			<nav className={styles.align_container}>
				<Link to="/favourites" className={styles.favourites}>
					<div className={theme === 'light' ? styles.icon : styles.icon_dark} />
					<p className={styles.text}>Избранное</p>
				</Link>
				<Theme />
			</nav>
		</>
	);
};

function Header() {
	const location = useLocation();
	const dispatch = useDispatch();
	const theme = useSelector(state => state.theme);

	return (
		<header className={styles.header}>
			<div className={styles.container}>
				<Link to="/">
					<button
						type="button"
						onClick={() => {
							dispatch(clearFiltered());
						}}
						className={styles.logo}
					>
						{theme === 'light' ? (
							<img className={styles.logo} src={logo} alt="Лого" />
						) : (
							<img className={styles.logo} src={logoDark} alt="Лого" />
						)}
					</button>
				</Link>

				{!['/signin', '/signup', '/profile'].some(path => location.pathname.match(path)) ? (
					<FullRenderedSection />
				) : (
					<nav className={styles.align_container}>
						{location.pathname.match('/profile') && (
							<div className={styles.profile}>
								<img
									src={theme === 'light' ? icon : iconDark}
									className={styles.profile_icon}
									alt="profile"
								/>
								<p className={styles.text}>pochta@email.ru</p>
							</div>
						)}
						<Theme />
					</nav>
				)}
			</div>
		</header>
	);
}

export default Header;
