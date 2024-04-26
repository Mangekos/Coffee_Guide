import HorizontalLine from '../HorizontalLine/HorizontalLine';
import styles from './NotFound.module.scss';

function NotFound() {
	return (
		<section className={styles.container}>
			{/* <HorizontalLine className={styles.line} /> */}
			<h1 className={styles.heading}>404</h1>
			<p className={styles.text}>такая страница не наӣдена :&#40; </p>
		</section>
	);
}

export default NotFound;
