import styles from './Form.module.scss';

function Form({ children, onSubmit }) {
	const handleSubmit = () => {
		onSubmit();
	};

	return (
		<form onSubmit={handleSubmit} className={styles.container}>
			{children}
		</form>
	);
}

export default Form;
