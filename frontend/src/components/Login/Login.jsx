import { useState } from 'react';
import { NavLink, useNavigate } from 'react-router-dom';
import { useForm } from 'react-hook-form';
import cn from 'classnames';
import styles from './Login.module.scss';
import { useLoginMutation } from '../../slices/apiSlice/apiSlice';
import { setUser } from '../../slices/userSlice/userSlice';

import Button from '../../assets/ui-kit/Button/Button';

function Login() {
	const navigate = useNavigate();

	const {
		register,
		watch,
		handleSubmit,
		reset,
		formState: { errors },
	} = useForm({ defaultValues: { email: '', password: '' }, mode: 'onChange' });

	const watchInputs = {
		password: 'coffee_git_project2024',
		username: 'admin_coffee_gid',
	};

	const [login, { isError }] = useLoginMutation();
	// const watchInputs = watch();
	console.log('watchInputs:', watchInputs);

	const handleLogin = async () => {
		if (watchInputs) {
			await login(watchInputs)
				// возвращает объект с ответом сервера
				.unwrap()
				.then(data => {
					if (data.auth_token) {
						localStorage.setItem('token', data.auth_token);
					}
					// console.log('token:', data.auth_token);
				})
				.catch(rejected => console.error(rejected));
			// setUser(inputValues);
		}
	};

	const onSubmit = data => {
		console.log(data);
		// navigate('/profile', { replace: true });
		reset();
	};
	const inputItemClassName = type => cn(styles.input, [errors[type] && styles.input_error]);

	return (
		<section className={styles.container}>
			<div className={styles.aligner}>
				<form className={styles.form} onSubmit={handleSubmit(onSubmit)}>
					<div className={styles.input_container}>
						<input
							{...register('email', { required: 'Необходимо ввести почту или ИНН' })}
							className={inputItemClassName('email')}
							placeholder="Почта / ИНН"
						/>
						{errors.email && <span className={styles.error}>{errors.email?.message}</span>}
					</div>
					<div className={styles.input_container}>
						<input
							type="password"
							{...register('password', {
								required: 'Необходимо ввести пароль',
							})}
							className={inputItemClassName('password')}
							placeholder="Пароль"
						/>
						{errors.password && <span className={styles.error}>{errors.password?.message}</span>}
					</div>
					<Button onClick={() => handleLogin()} type="submit" size="large" text="Войти" />
				</form>
				<div className={styles.links}>
					<p>Впервые у нас?</p>
					<NavLink to="/signup" className={styles.link}>
						Зарегистрироваться
					</NavLink>
				</div>
			</div>
			<p className={styles.text}>
				В случае если вы забыли пароль или у вас возникли вопросы, напишите нам admin@gmail.com
			</p>
		</section>
	);
}

export default Login;
