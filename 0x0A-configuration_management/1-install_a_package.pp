# installs puppet-lint
package {'puppet-lint':
  provider        => gem,
  install_options => [ '--force', '-v 2.5.0' ],
}
