// next.config.mjs
import withAntdLess from 'next-plugin-antd-less';

const nextConfig = withAntdLess({
  lessVarsFilePath: './styles/variables.less',
  webpack(config) {
    return config;
  },
});

export default nextConfig;
