AWS CDK: Github OIDC Provider

# P6CDGithubOIDCProvider

## LICENSE

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

## Other

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/p6m7g8/p6-cdk-github-oidc-provider) ![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=p6m78_p6-cdk-github-oidc-provider&metric=alert_status) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/p6m7g8/p6-cdk-github-oidc-provider) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/p6m7g8/p6-cdk-github-oidc-provider)

## Usage

```python
...
import { P6CDKGithubOIDCProvider } from 'p6-cdk-github-oidc-provider';

new P6CDKGithubOIDCProvider(this, 'SiteNameGithubOIDCProvider', {
  repo: string
});
```

## Architecture

![./assets/diagram.png](./assets/diagram.png)

## Author

Philip M. Gollucci [pgollucci@p6m7g8.com](mailto:pgollucci@p6m7g8.com)
