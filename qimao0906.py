import lzma, base64
exec(lzma.decompress(base64.b64decode('/Td6WFoAAATm1rRGAgAhARYAAAB0L+Wj4A+LB7BdADSbSme4Ujxz9O5cu+fYIzdp7+xsOJvxNpYPEUZxqhcjMGtvRwKudABozJUOeuMqcZfmztzcAd3NugkCkOzFBa/3/WZStOnSM5maHhMz0Zdp0x55dGm2ASF9MMsbROKJeHTRptLnkqlZkDqr9JV+AGIX/WpOFS/g2LmxyvriakhqwYC/+FeUKbQDPyy9PHhgtOrbWBScli/zPisUqml9J1hqxkkHyUFPE4cisco5dASRDGHpD1yMy0YTl1ewkyZHU6CQSfHppxjxTDkDHeiBNPtHhK7nX9JF6m69C5kdFpDnx0ky8y0e2WBYYFnZQlaStrD+/A28Ahuvi6mbj8TxeEAWGG8K2n/kIcR54Wc9DCFOhNHj8MvZ4ylAWzOD/4onXZYCkSc4V2Kl9m9VpJZOWuJJry5ct3czf0AGxfaNC+K5o3p10Qd9iOLNl4EESYB7RbU8Kq9ciiZ0KZw5aaDXaUv3B91GJH8JSBvMdxDopVZrSymJqgtMyGkNTdF3MYjmUch+9BPemlsL95X/kRq+LKodm37omB7JH7WFs4GkRTSDdWUqjWqz3ane9k2W+ezD2uqebDp6FtqLUf42HOn+z9Cpho+WhJFWVE3Bb9rmM0UErNeagUf5/oHeArnYawUj9/u1DoJmiGWhPsPgz3oTsNpP/PKcTwq2vzv18USAPlSKYWogXFqRLGohgpvHWfkaFWcwMCX+pP9hUYlRaRGOMHrzPFCpNX7Qwk42lE71b5RhQDbxJ9Kwz1tEnSokEYQEuDRmX0/H+8CF4jhhgV8l7+WU6YKB4zvCVoWOL0ebqlrdA88uYZBSSAJxgHnbvzKF31/DUfAU5FUgm5JjGJ/GWd6tUFLkEGX2OIZXOFpHf0sk+P8Kq5M1nNXFd/KyA0Wle3nyazbI/f2U44vSUbMHaAoOk4MTZJ8yEMm6zz6e7NDzuDSA45++PrQXpSpcdZjN9PYTU7phnO80AJCL956G1NJJ1O8JJir2+0hzJl2c4C2q83Bd6qgr3wqbLpaYx7oTd2yeAf6yTXJDzLFv42DyFQHFjOhgU/oC0rkrUq95bu3zaHvWwO2l+p+DL528Jva6iCmPoYxsNqX2HS4GuCzwJMK/MlKVrLP0YOi61tEqCCiu6bT/sKo5mktTnvf0MS9iKHWme3mmB4+pdYCLQll0Yq7vkZ8HJtPP0mTJo0mT+15T7ALM9CaJkmMG1GqB0ScajlQ6ZdZ3iGArs4LjM6dyFR1ILh41/gXr4qs293m2rnzIqqanRuIqD66AOR9qChiRuY2i+PPwy2w9fC9oZ5NVXFw4jYLuzX8bc6kOH6w1DWPZrgZolEqoRdjoyxwb7K2E2uJKgZZ4Pw48oQMnj3BtRqUhuFBb7rEmdpmPLVY3fmnyQL0CVy0LhFKNkUi9TRlQWjuPpMpz6lH7zBvn7qgLB63yNNmMTuQFFS2auow1g6HdM82ZLzm/7ZT98RnRJvV60zyDJ8aTrlCXOpUHHFlvHSMO8tSmimdseEitv6b52gzM7GNts+3qlPerB4W8tjisJKZJ8f1h3xhPo0up77EsKWNRxyxnvHC2KbBZ/C3tQPAxDq9Y+2tb/Z4ByvlCVpypXH+fG0DhlO8JSeLpb3vGaX6zCQGAQCwx79/GViH3ks9RyXXZEWKz5XQb2+SIeGMV8KJtowwK1+jc5zx0NnUdln4A11fBUsWpxr1lrFSw7nMdhaXYZaXIc7jXycmWQWgJyNRU7VTjhCRdHMtvh/XRDfIaWADbQd5GN7vL4CxW6gd9aIEaESqVHfnc+t4fzbZumfnbpJ8Qp56ifPUFPdzTZxPaArjDE/UgRVaBrYbrrzdym/qEj6t5gwwANc1Dms+EJeOEYwL3UBXB91bQfnDaqlqOn9vLKuhe3GoEXBhBWrSA66As/zn4kACQBQHwRTElwxGjdfm/+xPsaz3mEgifVzWHVr03QHz2PHs+HOOsjikSsY2EFQQWfwv0YfNf/Ow4KjA1QNTaeaTBNh4pujpmDfHyLgg5IIrqE+a+CGoBa3Jlbln9ThCkYDVFgMUyTKOIM0kub0v5Y6EqE6XWKqYrzXn5BJykhbJ+IdfgYxlhUMes+ubiFI4uqG2drtBXQFthdGCU8/jyDiiJO7PJMFPx5Fs/tr147gTwk4kshv3CMhxGgDRaoDKMXYWNlyjvtRpzEa1E2EeLcNDRCnzw7dlR+d036ZZYKhW3h+65uvxINsnL/CM6qzFLLzWiFM8yZEt8YprMn1a45M6dwWlvghAA0LkZrz9HpAVbnvImqtOX3BurTmq8ApZ6X8xbyEEw7anWw4J7JiS6dhKmodXNlSfAFxrIYD1/aXiwcS9yR/tQiVzW9NmEE2QV+lqVqGYYwGqFj3Md/MNbFDAGuBXtfqLyNu/q3ENVf7h1IerWAH8R/u1Pf6+GzSCT0blBZEfQqjSK5AlkofDhZ5xYZtGKIPfR2naXWzF9PcvBMmyrjdNU15euk4OyvUTx8PuWPYb2efMGw0EucObWq39PiwivYAlBzVCIK3IywYtjcz/hyA0bHSSznFl+022X8acpkMY79VGpUkFR4pfzrkk3DTLwTgMT1DEH0VwuIHXY4OgZZr2Y+yJAQuhOT2r+ZxH6kkprXuBuAABaJCXVqWaOqgABzA+MHwAADXDal7HEZ/sCAAAAAARZWg==')))
# Created by pyminifier (https://github.com/liftoff/pyminifier)

