module.exports = {
	env: {
		browser: true,
		es2023: true,
	},
	extends: [
		'airbnb',
		'eslint:recommended',
		'prettier',
		'plugin:react/recommended',
		'plugin:storybook/recommended',
	],
	overrides: [
		{
			env: {
				node: true,
			},
			files: ['.eslintrc.{js,cjs}'],
			parserOptions: {
				sourceType: 'script',
			},
		},
	],
	parserOptions: {
		ecmaVersion: 'latest',
		sourceType: 'module',
	},
	plugins: ['react', 'prettier'],
	rules: {
		'react/prop-types': 'off',
		'no-var': 'error',
		'prefer-const': 'warn',
		'no-unused-vars': 'off',
		'no-shadow': 'off',
		'no-unused-expressions': 'off',
		'react/react-in-jsx-scope': 'off',
		'prettier/prettier': ['warn', { endOfLine: 'auto' }],
		'import/prefer-default-export': 'off',
		'react/jsx-props-no-spreading': 'off',
		'react/function-component-definition': 'off',
		'react/button-has-type': 'off',
		'no-underscore-dangle': 'off',
		'class-methods-use-this': 'off',
		'jsx-a11y/no-noninteractive-element-interactions': 'off',
		'jsx-a11y/click-events-have-key-events': 'off',
		'no-param-reassign': 'off',
		'jsx-a11y/label-has-associated-control': 'off',
		'arrow-body-style': 'off',
	},
};
