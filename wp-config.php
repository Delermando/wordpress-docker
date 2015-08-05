<?php
/**
 * As configurações básicas do WordPress.
 *
 * Esse arquivo contém as seguintes configurações: configurações de MySQL, Prefixo de Tabelas,
 * Chaves secretas, Idioma do WordPress, e ABSPATH. Você pode encontrar mais informações
 * visitando {@link http://codex.wordpress.org/Editing_wp-config.php Editing
 * wp-config.php} Codex page. Você pode obter as configurações de MySQL de seu servidor de hospedagem.
 *
 * Esse arquivo é usado pelo script ed criação wp-config.php durante a
 * instalação. Você não precisa usar o site, você pode apenas salvar esse arquivo
 * como "wp-config.php" e preencher os valores.
 *
 * @package WordPress
 */

// ** Configurações do MySQL - Você pode pegar essas informações com o serviço de hospedagem ** //
/** O nome do banco de dados do WordPress */
define('DB_NAME', 'wordpress');

/** Usuário do banco de dados MySQL */
define('DB_USER', 'root');

/** Senha do banco de dados MySQL */
define('DB_PASSWORD', getenv('MYSQL_ENV_MYSQL_ROOT_PASSWORD'));

/** nome do host do MySQL */
define('DB_HOST', getenv('MYSQL_PORT_3306_TCP_ADDR'));


/** Conjunto de caracteres do banco de dados a ser usado na criação das tabelas. */
define('DB_CHARSET', 'utf8');

/** O tipo de collate do banco de dados. Não altere isso se tiver dúvidas. */
define('DB_COLLATE', '');

/**#@+
 * Chaves únicas de autenticação e salts.
 *
 * Altere cada chave para um frase única!
 * Você pode gerá-las usando o {@link https://api.wordpress.org/secret-key/1.1/salt/ WordPress.org secret-key service}
 * Você pode alterá-las a qualquer momento para desvalidar quaisquer cookies existentes. Isto irá forçar todos os usuários a fazerem login novamente.
 *
 * @since 2.6.0
 */
define('AUTH_KEY',         'n!e~#&@UK&-@^?$UW4M*> zJ;+voYR+6^Fa28-TE[@aK~39s%L5$]DwKE8KYe9:m');
define('SECURE_AUTH_KEY',  '[+^m`7sL4Z %H&C= t1/@hTv2bwe]mtF{O nI>Uj^f2MdJ+#Nn$}jj->3Gta~|Y9');
define('LOGGED_IN_KEY',    ';qy|hQ)an=8c`.[+MTW^lAzfAf!#T.x;+%7LWD[AHEDQz,j8?VCzoS1FMOq3i9tv');
define('NONCE_KEY',        'D4a,j(IV _*Hh JPG}w|4<E->TVT$g-juO}h)izc^w5SK;Uwd23Q;*8Hc#RRx#ko');
define('AUTH_SALT',        '`Y9u -+%s%UR|A5HTk }$umzLZ9@aT1MO,T3b3|jh%]QSUdF0=h15[V|D 07*7)y');
define('SECURE_AUTH_SALT', '*sLpaQI`MTg>9`M7,44{9<fHF7@IAu`h5|+BLKrX7cu^XiF{9+ 21R?> ,#K{]Ea');
define('LOGGED_IN_SALT',   '(K2uXW*gl45HazhaLS+W|[g)y#cbyqyOT0-1eI>ak|Dkw*UCh]+~Y~Z{~Uk1;fyd');
define('NONCE_SALT',       'ftn;I+}Sb+X}wV|Pr2.D`O=V]m-^3x7+}+TgIbGFQ6&M1E~lC&,.jl|%`|dFR/r4');

/**#@-*/

/**
 * Prefixo da tabela do banco de dados do WordPress.
 *
 * Você pode ter várias instalações em um único banco de dados se você der para cada um um único
 * prefixo. Somente números, letras e sublinhados!
 */
$table_prefix  = 'wp_';


/**
 * Para desenvolvedores: Modo debugging WordPress.
 *
 * altere isto para true para ativar a exibição de avisos durante o desenvolvimento.
 * é altamente recomendável que os desenvolvedores de plugins e temas usem o WP_DEBUG
 * em seus ambientes de desenvolvimento.
 */
define('WP_DEBUG', false);

/* Isto é tudo, pode parar de editar! :) */

/** Caminho absoluto para o diretório WordPress. */
if ( !defined('ABSPATH') )
    define('ABSPATH', dirname(__FILE__) . '/');

/** Configura as variáveis do WordPress e arquivos inclusos. */
require_once(ABSPATH . 'wp-settings.php');
