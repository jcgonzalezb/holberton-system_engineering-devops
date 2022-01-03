# Install puppet-lint version 2.5.0 using Puppet.

package { 'puppet-lint':
    ensure   => '2.5.0',
    name     => 'puppet-lint',
    provider => 'gem',
}
