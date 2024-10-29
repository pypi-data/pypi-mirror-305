AWS CDK: R53 -> CF -> S3

# P6CDKWebsitePlus

## LICENSE

[![License](https://img.shields.io/badge/License-Apache%202.0-yellowgreen.svg)](https://opensource.org/licenses/Apache-2.0)

## Other

[![Gitpod ready-to-code](https://img.shields.io/badge/Gitpod-ready--to--code-blue?logo=gitpod)](https://gitpod.io/#https://github.com/p6m7g8/p6-cdk-website-plus) ![Sonarcloud Status](https://sonarcloud.io/api/project_badges/measure?project=p6m7g8_p6-cdk-website-plus&metric=alert_status) ![GitHub commit activity](https://img.shields.io/github/commit-activity/y/p6m7g8/p6-cdk-website-plus) ![GitHub commit activity](https://img.shields.io/github/commit-activity/m/p6m7g8/p6-cdk-website-plus)

## Usage

```python
...
import { P6CDKWebsitePlus } from 'p6-cdk-website-plus';

new P6CDKWebsitePlus(this, 'WebsiteName', {
  hostedZoneName: 'gollucci.com',
  verifyEmail: 'pgollucci@p6m7g8.com',
  cloudfrontRecordName: 'www.gollucci.com',
});
```

## Architecture

![./assets/diagram.png](./assets/diagram.png)

## Author

Philip M. Gollucci [pgollucci@p6m7g8.com](mailto:pgollucci@p6m7g8.com)
