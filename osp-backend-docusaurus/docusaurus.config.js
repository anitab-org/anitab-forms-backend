module.exports = {
  title: 'Open Source Programs Backend Docs',
  tagline: 'Documentation for Open Source Programs Backend',
  url: 'https://osp-backend-docs.surge.sh/',
  baseUrl: '/',
  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',
  favicon: 'img/favicon.ico',
  organizationName: 'AnitaB.org', // Usually your GitHub org/user name.
  projectName: 'osp-backend-docusaurus', // Usually your repo name.
  themeConfig: {
    navbar: {
      title: 'Open Source Programs Backend',
      logo: {
        alt: 'AnitaB.org Logo',
        src: 'img/logo.png',
      },
      items: [
        {
          href:'https://www.anitab.org',
          label:'AnitaB.org',
          position:'right',
        },
        {
          href:'https://anitab-org.zulipchat.com/#narrow/stream/237907-open-source-progs',
          label:'Zulip',
          position:'right',
        },
        {
          href:'https://github.com/anitab-org/open-source-programs-backend',
          label:'Github',
          position:'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Docs',
          items: [
            {
              label: 'Frontend Docs',
              href:'https://osp-web-docs.surge.sh/',
            },
          ],
        },
        {
          title: 'Community',
          items: [
            {
              label: 'Zulip',
              href: 'https://anitab-org.zulipchat.com/#narrow/stream/237907-open-source-progs',
            },
            {
              label: 'Twitter',
              href: 'https://twitter.com/anitab_org',
            },
          ],
        },
        {
          title: 'More',
          items: [
            {
              label: 'Github',
              href: 'https://github.com/anitab-org/open-source-programs-backend',
            },
            {
              label: 'Blog',
              href: 'https://medium.com/anitab-org-open-source',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} Anita.Borg`,
    },
  },
  presets: [
    [
      '@docusaurus/preset-classic',
      {
        docs: {
          sidebarPath: require.resolve('./sidebars.js'),
          // Please change this to your repo.
          editUrl:
            'https://github.com/anitab-org/open-source-programs-backend/osp-backend-docusaurus',
        },
        theme: {
          customCss: require.resolve('./src/css/custom.css'),
        },
      },
    ],
  ],
};
